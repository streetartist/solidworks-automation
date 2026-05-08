# SetSaveToName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName`

Obsolete. Superseded by IPackAndGo::SetSaveToName2.
Obsolete. Superseded by [IPackAndGo::SetSaveToName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSaveToName( _
   ByVal Override As System.Boolean, _
   ByVal SaveToName As System.String _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim Override As System.Boolean
Dim SaveToName As System.String
Dim value As System.Boolean
 
value = instance.SetSaveToName(Override, SaveToName)
```

```

System.bool SetSaveToName( 
   System.bool Override,
   System.string SaveToName
)
```

```

System.bool SetSaveToName( 
   System.bool Override,
   System.String^ SaveToName
) 
```

#### Parameters

*Override*
:   True to override the paths and filenames of the documents set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md) or [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md), false to not

*SaveToName*
:   Path or the path and filename of the Zip file to use to override the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames

#### Return Value

True if the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames are overridden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetSaveToName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetSaveToName.md)  
[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.md)
