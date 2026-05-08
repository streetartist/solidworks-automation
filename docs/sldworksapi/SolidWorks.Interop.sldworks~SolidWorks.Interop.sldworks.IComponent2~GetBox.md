# GetBox Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox`

Gets the bounding box for component.
Gets the bounding box for component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBox( _
   ByVal IncludeRefPlanes As System.Boolean, _
   ByVal IncludeSketches As System.Boolean _
) As System.Object
```

```

Dim instance As IComponent2
Dim IncludeRefPlanes As System.Boolean
Dim IncludeSketches As System.Boolean
Dim value As System.Object
 
value = instance.GetBox(IncludeRefPlanes, IncludeSketches)
```

```

System.object GetBox( 
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
)
```

```

System.Object^ GetBox( 
   System.bool IncludeRefPlanes,
   System.bool IncludeSketches
) 
```

#### Parameters

*IncludeRefPlanes*
:   True includes reference planes with the returned bounding box, false does not

*IncludeSketches*
:   True includes sketches with the returned bounding box, false does not

#### Return Value

Object containing the two diagonal points that bound the component; the array contains 6 doubles

Remarks

The resulting box encloses the object, but it might not be the tightest box.

The X, Y, Z points returned by SOLIDWORKS are the lower- and upper-diagonal corners that bound the component with the box sides parallel to the X, Y and Z axes. SOLIDWORKS returns box dimensions that enclose the component and are typically close to the minimum possible size.

The return value is an array of doubles as follows:

**[** *XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2* **]**

It is possible for this method to return a NULL VARIANT for Dispatch. This occurs if your application calls IComponent2::GetBox with a component that represented a subassembly and that subassembly is not loaded.

The user interface behavior is the same. When the user selects a subassembly that is not loaded, there is no selection box around the subassembly. However, once the subassembly is loaded, there is a selection box.

**IMPORTANT:** The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

Example

[Get Assembly Bounding Box Using Components (VBA)](Get_Assembly_Bounding_Box_using_Components_Example_VB.htm)  
[Get Assembly Bounding Box Using Components (C#)](Get_Assembly_Bounding_Box_Using_Components_Example_CSharp.htm)  
[Get Assembly Bounding Box Using Components (VB.NET)](Get_Assembly_Bounding_Box_Using_Components_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.md)  
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.md)  
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.md)  
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.md)  
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.md)  
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.md)  
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.md)  
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.md)  
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.md)  
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md)  
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md)  
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md)  
[IPartDoc::GetPartBox Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPartBox.md)
