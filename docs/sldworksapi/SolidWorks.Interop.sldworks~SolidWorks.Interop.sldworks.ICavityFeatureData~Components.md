# Components Property (ICavityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~Components`

Gets or sets the design components for this cavity.
Gets or sets the design components for this cavity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Components As System.Object
```

```

Dim instance As ICavityFeatureData
Dim value As System.Object
 
instance.Components = value
 
value = instance.Components
```

```

System.object Components {get; set;}
```

```

property System.Object^ Components {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of design [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.md)  
[ICavityFeatureData::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetComponentsCount.md)  
[ICavityFeatureData::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~IGetComponents.md)  
[ICavityFeatureData::ISetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ISetComponents.md)
