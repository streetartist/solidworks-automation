# SetSize Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSize`

Sets the standard sheet size and the size of the sheet so that the drawing looks correct.
Sets the standard sheet size and the size of the sheet so that the drawing looks correct.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSize( _
   ByVal Size As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Size As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean
 
value = instance.SetSize(Size, Width, Height)
```

```

System.bool SetSize( 
   System.int Size,
   System.double Width,
   System.double Height
)
```

```

System.bool SetSize( 
   System.int Size,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*Size*
:   Paper size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Width*
:   Width of sheet

*Height*
:   Height of sheet

#### Return Value

True if the size of the sheet is set, false if not

Example

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)  
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md)  
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.md)  
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.md)  
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)
