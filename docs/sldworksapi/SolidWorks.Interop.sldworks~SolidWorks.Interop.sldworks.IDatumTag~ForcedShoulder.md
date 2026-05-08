# ForcedShoulder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~ForcedShoulder`

Gets whether this datum tag has a forced shoulder on its leader.
Gets whether this datum tag has a forced shoulder on its leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ForcedShoulder As System.Boolean
```

```

Dim instance As IDatumTag
Dim value As System.Boolean
 
value = instance.ForcedShoulder
```

```

System.bool ForcedShoulder {get;}
```

```

property System.bool ForcedShoulder {
   System.bool get();
}
```

#### Property Value

True if the datum tag has a forced shoulder on its leader, false if not

Remarks

If a square tag is attached to an edge that is not at a 0 or 90 angle, then the leader will always have a shoulder (bent leader). The user cannot remove the shoulder.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::Shoulder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~Shoulder.md)
