# Edge Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Edge`

Gets or sets the entity where to start the helix of this thread feature.
Gets or sets the entity where to start the helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Edge As Edge
```

```

Dim instance As IThreadFeatureData
Dim value As Edge
 
instance.Edge = value
 
value = instance.Edge
```

```

Edge Edge {get; set;}
```

```

property Edge^ Edge {
   Edge^ get();
   void set (    Edge^ value);
}
```

#### Property Value

Planar circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) (see **Remarks**)

Remarks

Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with Mark = 1 to select the edge.

If this property does not set a planar circular edge, then you must use [IThreadFeatureData::StartEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~StartEntity.md) to specify the start location of this thread's helix.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
