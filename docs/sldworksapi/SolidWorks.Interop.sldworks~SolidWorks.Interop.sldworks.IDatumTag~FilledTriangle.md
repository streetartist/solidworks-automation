# FilledTriangle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~FilledTriangle`

Gets or sets whether a filled triangle or empty triangle attaches to the model on the leader for this datum feature symbol.
Gets or sets whether a filled triangle or empty triangle attaches to the model on the leader for this datum feature symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FilledTriangle As System.Boolean
```

```

Dim instance As IDatumTag
Dim value As System.Boolean
 
instance.FilledTriangle = value
 
value = instance.FilledTriangle
```

```

System.bool FilledTriangle {get; set;}
```

```

property System.bool FilledTriangle {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this datum tag has a filled triangle, false if an empty triangle

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleAtIndex.md)  
[IDatumTag::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleCount.md)  
[IDatumTag::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTriangleAtIndex.md)
