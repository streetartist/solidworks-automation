# GetSolidHatchCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount`

Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data.
Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSolidHatchCount( _
   ByRef ArraySize As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Integer
 
value = instance.GetSolidHatchCount(ArraySize)
```

```

System.int GetSolidHatchCount( 
   out System.int ArraySize
)
```

```

System.int GetSolidHatchCount( 
   [Out] System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Number of solid-fill hatches

#### Return Value

Size of the array for the solid-fill hatches boundary data

Remarks

To get information about solid-fill hatches in drawing views, use [IView::GetFaceHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md), [IView::GetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md), and [IView::IGetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.md).

Example

[Get Solid-fill Hatch Information (VB.NET)](Get_Solid-fill_Hatch_Information_Example_VBNET.htm)  
[Get Solid-fill Hatch Information (VBA)](Get_Solid-fill_Hatch_Information_Example_VB6.htm)  
[Get Solid-fill Hatch Information (C#)](Get_Solid-fill_Hatch_Information_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.md)  
[IView::IGetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.md)  
[ISketch::GetSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches.md)
