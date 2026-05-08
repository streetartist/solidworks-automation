# CopyWizardHole Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CopyWizardHole`

Copies hole data from the source hole to the destination hole.
Copies hole data from the source hole to the destination hole.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyWizardHole( _
   ByVal SourceHole As System.Object, _
   ByVal DestinationHole As System.Object, _
   ByVal RebuildOwner As System.Boolean _
) As System.Integer
```

```

Dim instance As IModeler
Dim SourceHole As System.Object
Dim DestinationHole As System.Object
Dim RebuildOwner As System.Boolean
Dim value As System.Integer
 
value = instance.CopyWizardHole(SourceHole, DestinationHole, RebuildOwner)
```

```

System.int CopyWizardHole( 
   System.object SourceHole,
   System.object DestinationHole,
   System.bool RebuildOwner
)
```

```

System.int CopyWizardHole( 
   System.Object^ SourceHole,
   System.Object^ DestinationHole,
   System.bool RebuildOwner
) 
```

#### Parameters

*SourceHole*
:   [Source hole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

*DestinationHole*
:   [Destination hole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

*RebuildOwner*
:   True rebuilds the model, false does not

#### Return Value

0 if the call generated an error; 1 if the call did not generate an error

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICopyWizardHole Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICopyWizardHole.md)  
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)
