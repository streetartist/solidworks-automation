# CreateBreakOutSection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateBreakOutSection`

Creates a broken-out section in a drawing document.
Creates a broken-out section in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBreakOutSection( _
   ByVal Depth As System.Double _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Depth As System.Double
Dim value As System.Boolean
 
value = instance.CreateBreakOutSection(Depth)
```

```

System.bool CreateBreakOutSection( 
   System.double Depth
)
```

```

System.bool CreateBreakOutSection( 
   System.double Depth
) 
```

#### Parameters

*Depth*
:   Depth of the broken-out section

#### Return Value

True if the broken-out section was created, false if not

Example

[Create Broken-Out Section (VBA)](Create_BreakOut_Section_Example_VB.htm)  
[Create Broken-Out Section (VB.NET)](Create_BreakOut_Section_Example_VBNET.htm)  
[Create Broken-Out Section (C#)](Create_BreakOut_Section_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)
