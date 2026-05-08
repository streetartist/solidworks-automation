# WeldGap Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~WeldGap`

Gets and sets the weld gap of this corner member.
Gets and sets the weld gap of this corner member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WeldGap As System.Double
```

```

Dim instance As ICornerMember
Dim value As System.Double
 
instance.WeldGap = value
 
value = instance.WeldGap
```

```

System.double WeldGap {get; set;}
```

```

property System.double WeldGap {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Weld gap in meters between members; default is 0.0

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md)  
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.md)
