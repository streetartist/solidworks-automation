# Entities Property (ISurfaceKnitFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities`

Gets or sets the knitted faces and surfaces.
Gets or sets the knitted faces and surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Entities As System.Object
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Object
 
instance.Entities = value
 
value = instance.Entities
```

```

System.object Entities {get; set;}
```

```

property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of knit entities ([faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) and [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md))

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Get Knit Surface Data (VBA)](Get_Knit_Surface_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)  
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.md)  
[ISurfaceKnitFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.md)  
[ISurfaceKnitFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities.md)  
[ISurfaceKnitFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities.md)
