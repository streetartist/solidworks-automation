# DraftFromWall Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftFromWall`

Gets or sets whether to draft the rib from the wall interface or the sketch plane.
Gets or sets whether to draft the rib from the wall interface or the sketch plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DraftFromWall As System.Boolean
```

```

Dim instance As IRibFeatureData2
Dim value As System.Boolean
 
instance.DraftFromWall = value
 
value = instance.DraftFromWall
```

```

System.bool DraftFromWall {get; set;}
```

```

property System.bool DraftFromWall {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to draft from the sketch plane, false to draft from the wall interface

Remarks

This property is valid only when [IRibFeatureData2::EnableDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
