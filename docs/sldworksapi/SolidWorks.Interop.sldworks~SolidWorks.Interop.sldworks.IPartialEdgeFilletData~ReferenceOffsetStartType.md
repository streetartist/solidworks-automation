# ReferenceOffsetStartType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStartType`

Gets the type of offset reference for the start condition for this partial edge fillet.
Gets the type of [offset reference for the start condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.md) for this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceOffsetStartType As System.Integer
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Integer
 
value = instance.ReferenceOffsetStartType
```

```

System.int ReferenceOffsetStartType {get;}
```

```

property System.int ReferenceOffsetStartType {
   System.int get();
}
```

#### Property Value

Start condition offset reference type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)
