# Bodies Property (IDeleteBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies`

Gets or sets the bodies to delete or keep.
Gets or sets the bodies to delete or keep.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Bodies As System.Object
```

```

Dim instance As IDeleteBodyFeatureData
Dim value As System.Object
 
instance.Bodies = value
 
value = instance.Bodies
```

```

System.object Bodies {get; set;}
```

```

property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to delete or keep

Remarks

Call [IDeleteBodyFeatureData::KeepBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~KeepBodies.md) to specify whether to keep or delete the bodies.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md)  
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.md)  
[IDeleteBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.md)  
[IDeleteBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.md)  
[IDeleteBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.md)
