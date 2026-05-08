# GetBalloonPadding Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonPadding`

Gets the balloon padding of this note.
Gets the balloon padding of this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBalloonPadding() As System.Double
```

```

Dim instance As INote
Dim value As System.Double
 
value = instance.GetBalloonPadding()
```

```

System.double GetBalloonPadding()
```

```

System.double GetBalloonPadding(); 
```

#### Return Value

Balloon padding

Remarks

This method is valid only if [INote::GetBalloonSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.md) is set to [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html).swBF\_Tightest.

Example

[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)  
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)  
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::SetBalloonPadding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloonPadding.md)  
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md)
