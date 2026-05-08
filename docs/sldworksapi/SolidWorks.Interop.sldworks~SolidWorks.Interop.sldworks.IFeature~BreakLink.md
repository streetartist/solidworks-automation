# BreakLink Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~BreakLink`

Breaks the link to third-party native CAD parts and assemblies.
Breaks the link to third-party native CAD parts and assemblies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function BreakLink( _
   ByVal AllComponents As System.Boolean, _
   ByVal Silent As System.Boolean _
) As System.Integer
```

```

Dim instance As IFeature
Dim AllComponents As System.Boolean
Dim Silent As System.Boolean
Dim value As System.Integer
 
value = instance.BreakLink(AllComponents, Silent)
```

```

System.int BreakLink( 
   System.bool AllComponents,
   System.bool Silent
)
```

```

System.int BreakLink( 
   System.bool AllComponents,
   System.bool Silent
) 
```

#### Parameters

*AllComponents*
:   True to break the link for all subcomponents within a top-level subassembly, false to not (see **Remarks**)

*Silent*
:   True to suppress dialog windows, false to not

#### Return Value

Error codes as defined in [sw3DInterconnectImportErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

Remarks

By default, breaking a link of an assembly component breaks the links of all instances of that component.

After you break a link, all references to the original CAD file are lost. You can no longer change the entities to transfer from the original file or update the SOLIDWORKS model with changes from the third-party authoring application.

Example

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.md)
