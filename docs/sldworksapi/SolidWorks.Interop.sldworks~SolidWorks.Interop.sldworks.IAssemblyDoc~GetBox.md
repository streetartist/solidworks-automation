# GetBox Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox`

Gets the bounding box.
Gets the bounding box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBox( _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.GetBox(Options)
```

```

System.object GetBox( 
   System.int Options
)
```

```

System.Object^ GetBox( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Type of bounding box as defined by [swBoundingBoxOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBoundingBoxOptions_e.html)

#### Return Value

Object containing the two diagonal points that bound the component; the array contains 6 doubles (see **Remarks**)

Remarks

**IMPORTANT:** The values returned are approximate and should not be used for comparison  
or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.The resulting box encloses the object, but it might not be the tightest box.

The X, Y, Z points returned by SOLIDWORKS are the lower- and upper-diagonal corners that bound the component with the box sides parallel to the X, Y and Z axes. SOLIDWORKS returns box dimensions that enclose the object and are typically close to the minimum possible size.

The return value is an array of doubles as follows:

> **[** *XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2* **]**

Example

[Get Assembly Bounding Box Using Assembly (C#)](Get_Assembly_Bounding_Box_Using_Assembly_Example_CSharp.htm)  
[Get Assembly Bounding Box Using Assembly (VB.NET)](Get_Assembly_Bounding_Box_Using_Assembly_Example_VBNET.htm)  
[Get Assembly Bounding Box Using Assembly (VBA)](Get_Assembly_Bounding_Box_using_Assembly_Example_VB.htm)  
[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)  
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)  
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md)  
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md)  
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md)  
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.md)  
[IAssemblyDoc::UpdateBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox.md)  
[IBody2::GetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.md)  
[IBody2::IGetBodyBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.md)  
[IComponent2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBox.md)  
[IComponent2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBox.md)  
[IFace2::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.md)  
[IFace2::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.md)  
[IFeature::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBox.md)  
[IFeature::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBox.md)
