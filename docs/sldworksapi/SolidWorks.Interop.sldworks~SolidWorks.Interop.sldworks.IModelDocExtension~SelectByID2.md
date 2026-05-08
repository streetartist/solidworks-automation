# SelectByID2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2`

Selects the specified entity.
Selects the specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByID2( _
   ByVal Name As System.String, _
   ByVal Type As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout, _
   ByVal SelectOption As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim Type As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim SelectOption As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByID2(Name, Type, X, Y, Z, Append, Mark, Callout, SelectOption)
```

```

System.bool SelectByID2( 
   System.string Name,
   System.string Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout Callout,
   System.int SelectOption
)
```

```

System.bool SelectByID2( 
   System.String^ Name,
   System.String^ Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout^ Callout,
   System.int SelectOption
) 
```

#### Parameters

*Name*
:   Name of object to select or an empty string

*Type*
:   Type of object (uppercase) as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) or an empty string

*X*
:   X selection location or 0

*Y*
:   Y selection location or 0

*Z*
:   Z selection location or 0

*Append*
:   | If... | An, if entity is... | Then... |
    | --- | --- | --- |
    | True | Not already selected | Entity is appended to the current selection list |
    |  | Already selected | Entity is removed from the current selection list |
    | False | Not already selected | Current selection is cleared and then the entity is put on the list |
    |  | Already selected | Current selection list remains the same |

*Mark*
:   Value that you want to use as a mark; this value is used by other functions that require ordered selection (see **Remarks**)

*Callout*
:   Pointer to the associated [callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)

*SelectOption*
:   Selection option as defined in [swSelectOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectOption_e.html) (see **Remarks**)

#### Return Value

True if item was successfully selected, false if not

Remarks

Use this method instead of using the selection methods on the following objects:

- [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)
- [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)
- [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)
- [IFeatureManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)
- [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)
- [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)
- [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)
- [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)

The previously listed objects' selection methods do not work well when a PropertyManager page is open or a command is running. This method, IModelDocExtension::SelectByID2, handles selection correctly regardless if a command is running.

If your application already has an object handle (for example, IFace2), use the appropriate Select method to select the item directly using its handle.

To filter the objects selected by this method, set the Type parameter. If no filtering is required, then pass an empty string for this parameter.

For example, to select an object of type swSelDIMENSIONS, use the string that appears in the comment column, "DIMENSION". The objectType might change based on your current state. For example, to select a sketch point that was created in the active sketch, specify Type as "SKETCHPOINT". However, if you do not have an active sketch, or if the point was created in a sketch other than the active sketch, or the point is the origin point, then specify Type as "EXTSKETCHPOINT".

If Type is specified, then this method returns false if it cannot find the matching object type.

The Name parameter is not intended for selection of faces, edges, and so on. This is a case-sensitive string for objects that are automatically named by SOLIDWORKS during entity creation, such as dimensions, drawing views, and so on. This method tries to find and select an object whose name matches the Name parameter; however, the match needs to be exact for this method to return true.

For example:

- If a string is passed that matches an object name but whose case does not match exactly, then this method could return false. For selection of dimensions, the Name parameter must be fully qualified.
- Specify "D1@Sketch2@Part1.SLDPRT" rather than "D1@Sketch2"; otherwise, this method could return false. If you do not know the object name, or if it is an item that is not automatically named by SOLIDWORKS, you can pass an empty string.

If you are using the Name parameter, then specify the x, y, and z  coordinates in terms of the context where the item was created. For example, if you want to select a sketch point using its name (for example, "Point1") in the Name parameter, then specify X, Y, and Z in terms of the sketch where the point was created. Even if the sketch is not active, specify the X, Y, and Z values in terms of sketch space when you use the Name parameter. In certain situations, you can also pass in the x, y, and z coordinates as (0,0,0). For example, to select a feature shown in the FeatureManager design tree, you do not need to specify x, y, and z coordinates. However, to select objects such as faces or when you need a point location picked, you must specify the x, y, and z coordinates. If you are not using the Name parameter as a filter, then specify the x, y, and z coordinates in terms of model space. The coordinates are used when the object name is not provided, and the coordinates are dependent on the view state.

If you do not know the object name or the object type, pass empty strings for the Name and Type parameters. The selection routine makes the best attempt to select the correct object.

To get [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) objects by name, use [IPartDoc::GetEntityByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.md) or [IPartDoc::IGetEntityByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.md).

For SelectOption, specify swSelectOption\_e.swSelectOptionDefault to indicate that the Shift key is not used during selection or specify swSelectOption\_e.swSelectOptionExtensive to indicate that the Shift key is used during selection.

The [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object used to call this method must be an open and visible document. For example, you cannot use the IModelDoc2 object returned from an assembly component ([IComponent2::GetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc.md) or [IComponent2::IGetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelDoc.md)) unless that SOLIDWORKS component part or subassembly is an open and visible document. In this case, you can select the item using the fully qualified name (for example, "Plane4@Part1-1@Assem1").

When selecting IFace2 objects, this method uses the specified point as input to the normal user-interface selection routines to use the speed of ray tracing. As a result, if the view changes from the original recorded size or orientation, then the same IFace2 might not be selected next time. If your application has a pointer to the IFace2 object to be selected, then you can call the [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md) method directly. Otherwise, you can call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md). Calling either of these methods allows for tighter control over the starting point and the direction in which to search. IModelDocExtension::SelectByRay is recorded when IModelDocExtension::SelectByID2 relies on the selection coordinates and prone to failure if the model view is altered.

Use:

- Mark of 4 when selecting multiple edges or sketch segments and grouping them into one object for the path for a sweep feature. See the **Select Multiple Sketch Segments for Sweep Path** examples.
- Mark of 2 when selecting multiple edges, sketch segments, or curves and grouping them into one object for the guide curves for a loft feature. See the **Select Multiple Splines for Loft Guide Curves** examples.
- [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) and [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md) to add objects to a selection list without preselecting the objects in the user interface.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Add Distance Mates (VBA)](Add_Distance_Mates_Example_VB.htm)  
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Get Selected Object (VBA)](Get_Selected_Object_Example_VB.htm)  
[Insert Wrap Feature (VBA)](Insert_Wrap_Feature_Example_VB.htm)  
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)  
[Connect to SOLIDWORKS Session (C#)](Connect_to_SOLIDWORKS_Session_CSharp.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)  
[Select Multiple Sketch Segments for Sweep Path (C#)](Select_Multiple_Paths_for_Sweep_Path_Example_CSharp.htm)  
[Select Multiple Sketch Segments for Sweep Path (VB.NET)](Select_Multiple_Paths_for_Sweep_Path_Example_VBNET.htm)  
[Select Multiple Sketch Segments for Sweep Path (VBA)](Select_Multiple_Paths_for_Sweep_Path_Example_VB.htm)  
[Select Multiple Splines for Loft Guide Curves (C#)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_CSharp.htm)  
[Select Multiple Splines for Loft Guide Curves (VB.NET)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VBNET.htm)  
[Select Multiple Splines for Loft Guide Curves (VBA)](Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::MultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.md)  
[IModelDocExtension::IMultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.md)  
[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[IFeature::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)  
[IAssemblyDoc::SelectComponentsBySize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize.md)  
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)
