# Body Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~Body`

Gets or sets the body where the rib is created.
Gets or sets the body where the rib is created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Body As Body2
```

```

Dim instance As IRibFeatureData2
Dim value As Body2
 
instance.Body = value
 
value = instance.Body
```

```

Body2 Body {get; set;}
```

```

property Body2^ Body {
   Body2^ get();
   void set (    Body2^ value);
}
```

#### Property Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) where rib is created

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
