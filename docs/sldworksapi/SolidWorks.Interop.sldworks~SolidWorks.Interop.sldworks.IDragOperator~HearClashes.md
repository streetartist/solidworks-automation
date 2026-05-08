# HearClashes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HearClashes`

Gets or sets whether sound is associated with entity clashes.
Gets or sets whether sound is associated with entity clashes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HearClashes As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.HearClashes = value
 
value = instance.HearClashes
```

```

System.bool HearClashes {get; set;}
```

```

property System.bool HearClashes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the sound for clashes is enabled, false if it is disabled

Remarks

This property enables audio feedback when collisions occur between components selected for collision detection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::HighlightClashes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HighlightClashes.md)
