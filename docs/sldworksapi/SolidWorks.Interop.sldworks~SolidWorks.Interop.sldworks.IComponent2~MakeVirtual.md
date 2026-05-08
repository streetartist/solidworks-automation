# MakeVirtual Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual`

Obsolete. by Superseded by IComponent2::MakeVirtual2.
Obsolete. by Superseded by [IComponent2::MakeVirtual2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeVirtual() As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
value = instance.MakeVirtual()
```

```

System.bool MakeVirtual()
```

```

System.bool MakeVirtual(); 
```

#### Return Value

True if this component is saved in an assembly, false if not

Remarks

This method breaks the link to the external component file. Existing references are ignored, and the component is renamed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
