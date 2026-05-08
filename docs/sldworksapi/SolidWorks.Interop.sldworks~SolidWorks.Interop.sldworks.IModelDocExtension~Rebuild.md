# Rebuild Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Rebuild`

Rebuilds the model in assembly and drawing documents and returns the status of the rebuild.
Rebuilds the model in assembly and drawing documents and returns the status of the rebuild.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Rebuild( _
   ByVal Options As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Boolean
 
value = instance.Rebuild(Options)
```

```

System.bool Rebuild( 
   System.int Options
)
```

```

System.bool Rebuild( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Type of rebuild as defined in [swRebuildOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOptions_e.html)

#### Return Value

True if the rebuild is successful, false if not

Remarks

Use [IModelDoc2::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.md) to check the type of document.

Example

[Rebuild an Assembly (VBA)](Rebuild_an_Assembly_Example_VB.htm)  
[Rebuild an Assembly (VB.NET)](Rebuild_an_Assembly_Example_VBNET.htm)  
[Rebuild an Assembly (C#)](Rebuild_an_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDoc2::ForceRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)  
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.md)  
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.md)
