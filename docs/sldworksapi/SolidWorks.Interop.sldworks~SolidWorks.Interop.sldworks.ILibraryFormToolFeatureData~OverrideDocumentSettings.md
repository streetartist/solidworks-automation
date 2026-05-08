# OverrideDocumentSettings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings`

Specifies the flat pattern visibility options for this forming tool feature.
Specifies the flat pattern visibility options for this forming tool feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub OverrideDocumentSettings( _
   ByVal OverrideSettings As System.Boolean, _
   ByVal ShowPunch As System.Boolean, _
   ByVal ShowProfile As System.Boolean, _
   ByVal ShowCenter As System.Boolean _
) 
```

```

Dim instance As ILibraryFormToolFeatureData
Dim OverrideSettings As System.Boolean
Dim ShowPunch As System.Boolean
Dim ShowProfile As System.Boolean
Dim ShowCenter As System.Boolean
 
instance.OverrideDocumentSettings(OverrideSettings, ShowPunch, ShowProfile, ShowCenter)
```

```

void OverrideDocumentSettings( 
   System.bool OverrideSettings,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter
)
```

```

void OverrideDocumentSettings( 
   System.bool OverrideSettings,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter
) 
```

#### Parameters

*OverrideSettings*
:   True to override the options set in **Tools > Options > Document Properties > Sheet Metal**, false to not (see **Remarks**)

*ShowPunch*
:   True to display the cut of this forming tool when the part is flattened, false to not (see **Remarks**)

*ShowProfile*
:   True to display the placement sketch of this forming tool when the part is flattened, false to not (see **Remarks**)

*ShowCenter*
:   True to display the center mark where this forming tool is located in the flat pattern, false to not (see **Remarks**)

Remarks

ShowPunch, ShowProfile, and ShowCenter are valid only if OverrideSettings is set to true.

Example

See the [ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)  
[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)  
[ILibraryFormToolFeatureData::OverrideSettings Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideSettings.md)  
[ILibraryFormToolFeatureData::ShowCenter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowCenter.md)  
[ILibraryFormToolFeatureData::ShowProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowProfile.md)  
[ILibraryFormToolFeatureData::ShowPunch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ShowPunch.md)
