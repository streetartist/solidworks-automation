# HighlightClashes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HighlightClashes`

Gets or sets whether to highlight clashes.
Gets or sets whether to highlight clashes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HighlightClashes As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.HighlightClashes = value
 
value = instance.HighlightClashes
```

```

System.bool HighlightClashes {get; set;}
```

```

property System.bool HighlightClashes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if clash highlighting is enabled, false if it is disabled

Remarks

This property enables visual feedback when collisions occur between components selected for collision detection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::HearClashes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HearClashes.md)
