# LeaderOrientation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~LeaderOrientation`

Gets or sets the orientation of the leader for a round datum tag.
Gets or sets the orientation of the leader for a round datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LeaderOrientation As System.Integer
```

```

Dim instance As IDatumTag
Dim value As System.Integer
 
instance.LeaderOrientation = value
 
value = instance.LeaderOrientation
```

```

System.int LeaderOrientation {get; set;}
```

```

property System.int LeaderOrientation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Orientation as defined in [swDatumGbLeaderStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumGbLeaderStyle_e.html)

Remarks

Although you get or set this property at any time, this property only applies to round datum tags. If you use it when a square datum tag is shown, you will not see a value for the current display.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)
