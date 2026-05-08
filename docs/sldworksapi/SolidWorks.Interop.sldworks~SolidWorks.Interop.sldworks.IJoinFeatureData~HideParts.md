# HideParts Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~HideParts`

Gets or sets whether the original components are hidden after joined.
Gets or sets whether the original components are hidden after joined.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HideParts As System.Boolean
```

```

Dim instance As IJoinFeatureData
Dim value As System.Boolean
 
instance.HideParts = value
 
value = instance.HideParts
```

```

System.bool HideParts {get; set;}
```

```

property System.bool HideParts {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the original components are hidden after joined, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)  
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.md)
