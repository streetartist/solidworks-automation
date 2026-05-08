# Shoulder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~Shoulder`

Gets whether there is a shoulder (or bend) in the leader for this datum tag.
Gets whether there is a shoulder (or bend) in the leader for this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Shoulder As System.Boolean
```

```

Dim instance As IDatumTag
Dim value As System.Boolean
 
instance.Shoulder = value
 
value = instance.Shoulder
```

```

System.bool Shoulder {get; set;}
```

```

property System.bool Shoulder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this datum tag has a shoulder, false if not

Remarks

Although you get or set this property at any time, this property only applies to square datum tags. If you use it when a round datum tag is shown, you will not see a value for the current display.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::ForcedShoulder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~ForcedShoulder.md)
