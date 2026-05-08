# ScaleHatchPattern Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern`

Gets or sets whether to scale the hatch pattern to the drawing view.
Gets or sets whether to scale the hatch pattern to the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleHatchPattern As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.ScaleHatchPattern = value
 
value = instance.ScaleHatchPattern
```

```

System.bool ScaleHatchPattern {get; set;}
```

```

property System.bool ScaleHatchPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to scale the hatch pattern to the drawing view, false to not

Example

[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)  
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)  
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFaceHatchCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md)  
[IView::GetFaceHatches Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md)  
[IModelDoc2::InsertHatchedFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.md)
