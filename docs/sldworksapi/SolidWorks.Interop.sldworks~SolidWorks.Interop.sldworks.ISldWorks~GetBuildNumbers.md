# GetBuildNumbers Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers`

Obsolete. Superseded by ISldWorks::GetBuildNumbers2.
Obsolete. Superseded by [ISldWorks::GetBuildNumbers2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetBuildNumbers( _
   ByRef BaseVersion As System.String, _
   ByRef CurrentVersion As System.String _
) 
```

```

Dim instance As ISldWorks
Dim BaseVersion As System.String
Dim CurrentVersion As System.String
 
instance.GetBuildNumbers(BaseVersion, CurrentVersion)
```

```

void GetBuildNumbers( 
   out System.string BaseVersion,
   out System.string CurrentVersion
)
```

```

void GetBuildNumbers( 
   [Out] System.String^ BaseVersion,
   [Out] System.String^ CurrentVersion
) 
```

#### Parameters

*BaseVersion*
:   SOLIDWORKS major revision number

*CurrentVersion*
:   SOLIDWORKS build number

Example

**Visual Basic for Applications (VBA)**

'-------------------------

Option Explicit

Dim swApp as SldWorks.SldWorks

Dim BaseVersion as String

Dim CurrentVersion as String

Sub main()

Set swApp = Application.SldWorks

swApp.**GetBuildNumbers** BaseVersion, CurrentVersion

Debug.Print "SOLIDWORKS major revision number: " & BaseVersion

Debug.Print "SOLIDWORKS build number: " & CurrentVersion

End Sub

'------------------------------------------

**Output**

SOLIDWORKS major revision number: SW2009\_a1

SOLIDWORKS build number: d080407.062

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md)  
[ISldWorks::IGetVersionHistoryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount.md)  
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md)  
[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.md)
