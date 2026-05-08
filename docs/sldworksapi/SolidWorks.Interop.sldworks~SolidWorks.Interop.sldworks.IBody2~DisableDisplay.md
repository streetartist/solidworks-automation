# DisableDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisableDisplay`

Gets or sets whether to hide or show this body.
Gets or sets whether to hide or show this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisableDisplay As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
instance.DisableDisplay = value
 
value = instance.DisableDisplay
```

```

System.bool DisableDisplay {get; set;}
```

```

property System.bool DisableDisplay {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to hide the body; false to show the body  
  
**NOTE:** If true, then the body is hidden but remains selectable.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::HideBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.md)  
[IModelDoc2::HideShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideShowBodies.md)  
[IModelDoc2::HideSolidBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideSolidBody.md)  
[IFeatureManager::ShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowBodies.md)  
[IFeatureManager::HideBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.md)
