# NeedsRebuild2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2`

Gets whether the model document needs to be rebuilt.
Gets whether the model document needs to be rebuilt.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property NeedsRebuild2 As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
value = instance.NeedsRebuild2
```

```

System.int NeedsRebuild2 {get;}
```

```

property System.int NeedsRebuild2 {
   System.int get();
}
```

#### Property Value

Rebuild status of model document as defined in [swModelRebuildStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModelRebuildStatus_e.html)

Example

[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)  
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)  
[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)  
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.md)  
[IConfiguration::AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.md)  
[IConfiguration::NeedsRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.md)  
[IModelDocExtension::ShowPartRebuildIndicators Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowPartRebuildIndicators.md)  
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)
