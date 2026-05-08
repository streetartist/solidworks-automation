# GetFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFormat`

Gets the format type of this Gtol.
Gets the format type of this Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFormat() As System.Integer
```

```

Dim instance As IGtol
Dim value As System.Integer
 
value = instance.GetFormat()
```

```

System.int GetFormat()
```

```

System.int GetFormat(); 
```

#### Return Value

Type of Gtol format as defined by [swGtolFormatType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatType_e.html)

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
