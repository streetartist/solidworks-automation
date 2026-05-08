# GetCorresponding Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorresponding`

Gets the object in this drawing view that corresponds to the specified part or assembly object.
Gets the object in this drawing view that corresponds to the specified part or assembly object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorresponding( _
   ByVal InputObject As System.Object _
) As System.Object
```

```

Dim instance As IView
Dim InputObject As System.Object
Dim value As System.Object
 
value = instance.GetCorresponding(InputObject)
```

```

System.object GetCorresponding( 
   System.object InputObject
)
```

```

System.Object^ GetCorresponding( 
   System.Object^ InputObject
) 
```

#### Parameters

*InputObject*
:   Pointer to the Dispatch object in a part or assembly (see **Remarks**)

#### Return Value

Pointer to the corresponding object in this drawing view; null or Nothing if none found

Remarks

InputObject can be any object assigned a persistent reference or object ID; for example, [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md),  [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md), etc.

Annotation objects will be found only if they were previously imported into this drawing view.

Use [IModelDocExtension::GetCorresponding2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.md) to get the part or assembly object that corresponds to an object in a drawing view.

Example

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCorrespondingEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.md)
