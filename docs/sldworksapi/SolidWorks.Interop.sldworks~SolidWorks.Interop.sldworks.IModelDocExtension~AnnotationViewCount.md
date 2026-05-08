# AnnotationViewCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViewCount`

Gets the number of annotation views in this part or assembly document.
Gets the number of annotation views in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AnnotationViewCount As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
value = instance.AnnotationViewCount
```

```

System.int AnnotationViewCount {get;}
```

```

property System.int AnnotationViewCount {
   System.int get();
}
```

#### Property Value

Number of annotation views in this model document

Remarks

Call this method before calling [IModelDocExtension::IGetAnnotationViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.md) to get the size of the array for that method.

Example

[Move Annotations to Notes Area Annotation View (C#)](Move_Annotations_to_First_Annotation_View_Example_CSharp.htm)  
[Move Annotations to Notes Area Annotation View (VB.NET)](Move_Annotations_to_First_Annotation_View_Example_VBNET.htm)  
[Move Annotations to Notes Area Annotation View (VBA)](Move_Annotations_to_First_Annotation_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetAnnotationViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetAnnotationViews.md)  
[IModelDocExtension::AnnotationViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AnnotationViews.md)
