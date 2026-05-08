# TrimOrder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~TrimOrder`

Gets and sets the trim order of this corner member.
Gets and sets the trim order of this corner member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TrimOrder As System.Integer
```

```

Dim instance As ICornerMember
Dim value As System.Integer
 
instance.TrimOrder = value
 
value = instance.TrimOrder
```

```

System.int TrimOrder {get; set;}
```

```

property System.int TrimOrder {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Trim order

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md)  
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.md)
