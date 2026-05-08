# AddFrame Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~AddFrame`

Adds a frame at the end of the list of this Gtol's frames.
Adds a frame at the end of the list of this Gtol's frames.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddFrame() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.AddFrame()
```

```

System.bool AddFrame()
```

```

System.bool AddFrame(); 
```

#### Return Value

True if frame successfully added, false if not

Remarks

This method is valid only if this Gtol was created in SOLIDWORKS 2022 or later.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
