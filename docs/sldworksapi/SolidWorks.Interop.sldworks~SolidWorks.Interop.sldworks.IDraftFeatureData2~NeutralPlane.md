# NeutralPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~NeutralPlane`

Gets or sets the neutral plane for this draft feature.
Gets or sets the neutral plane for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NeutralPlane As System.Object
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Object
 
instance.NeutralPlane = value
 
value = instance.NeutralPlane
```

```

System.object NeutralPlane {get; set;}
```

```

property System.Object^ NeutralPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Face to serve as the neutral plane

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)
