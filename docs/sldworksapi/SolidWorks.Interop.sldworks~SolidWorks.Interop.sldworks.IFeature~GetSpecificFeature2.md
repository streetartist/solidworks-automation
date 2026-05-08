# GetSpecificFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2`

Gets the more specific interface to a selected feature.
Gets the more specific interface to a selected feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSpecificFeature2() As System.Object
```

```

Dim instance As IFeature
Dim value As System.Object
 
value = instance.GetSpecificFeature2()
```

```

System.object GetSpecificFeature2()
```

```

System.Object^ GetSpecificFeature2(); 
```

#### Return Value

Specific interface (see **Remarks**)

Remarks

This method gets these interfaces to a corresponding selected feature:

|  |  |
| --- | --- |
| - [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) - [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) - [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) - [ICamera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md) - [ICommentFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md) - [ICosmeticWeldBeadFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.md) - [IDetailCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md) - [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) - [IFeatureFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md) - [IFlatPatternFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder.md) - [ILight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight.md) - [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md) - [IMateInPlace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.md) | - [IMateReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md) - [IMidSurface3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md) - [IProfileGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.md) - [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) - [IReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md) - [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) - [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md) - [ISelectionSetFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.md) - [ISensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  - [ISheetMetalFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder.md) - [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) - [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) - [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) - [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) - [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md) - [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md) |

| **If...** | **Then...** |
| --- | --- |
| You start with an IFeature object and want to get a more specific object | A call to IFeature::GetSpecificFeature2 is required. If you have the more specific object, then a call to QueryInterface in C++ or an assignment to a IFeature-typed variable allows an application to get back to the IFeature object. |
| You are writing a Dispatch application | You can use [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) or [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) to identify the type of Dispatch object returned so that you can call the appropriate properties and methods for that object. |
| You are writing a COM application | You can use the return value with QueryInterface to determine the object returned. |
| No interface exists or there is no specific object for the type of feature | This method returns Nothing or null. |

For some feature types, this method returns Nothing or null because there is no specific object for that type of feature (e.g., features such as extrusions, lofts, fillets, chamfers, etc.). For these types of features, call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get their feature data objects.

For other entities selected in the FeatureManager design tree, you must know its interface in advance and cast the return value of [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) to the correct interface.

For all functions that return objects, always check whether the return value is Nothing or null before you try to use it.

Example

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)  
[Determine if Sketch Suitable for Feature (VBA)](Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm)  
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)  
[Get Parameters for Reference Axis (VBA)](Get_Parameters_for_Reference_Axis_Example_VB.htm)  
[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)  
[Insert and Position DXF File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)  
[Get Areas of MidSurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)  
[Get Areas of MidSurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)  
[Get Areas of MidSurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
