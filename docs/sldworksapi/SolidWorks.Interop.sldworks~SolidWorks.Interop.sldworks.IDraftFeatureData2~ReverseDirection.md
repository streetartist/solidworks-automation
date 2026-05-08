# ReverseDirection Property (IDraftFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ReverseDirection`

Gets or sets whether the direction of the draft feature is reversed.
Gets or sets whether the direction of the draft feature is reversed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseDirection As System.Boolean
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Boolean
 
instance.ReverseDirection = value
 
value = instance.ReverseDirection
```

```

System.bool ReverseDirection {get; set;}
```

```

property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True reverses the direction of the draft feature, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)
