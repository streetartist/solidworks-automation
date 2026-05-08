# GetBuildNumbers2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2`

Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application.
Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetBuildNumbers2( _
   ByRef BaseVersion As System.String, _
   ByRef CurrentVersion As System.String, _
   ByRef HotFixes As System.String _
) 
```

```

Dim instance As ISldWorks
Dim BaseVersion As System.String
Dim CurrentVersion As System.String
Dim HotFixes As System.String
 
instance.GetBuildNumbers2(BaseVersion, CurrentVersion, HotFixes)
```

```

void GetBuildNumbers2( 
   out System.string BaseVersion,
   out System.string CurrentVersion,
   out System.string HotFixes
)
```

```

void GetBuildNumbers2( 
   [Out] System.String^ BaseVersion,
   [Out] System.String^ CurrentVersion,
   [Out] System.String^ HotFixes
) 
```

#### Parameters

*BaseVersion*
:   SOLIDWORKS major revision number

*CurrentVersion*
:   SOLIDWORKS build number

*HotFixes*
:   SOLIDWORKS hot fix numbers

Example

[Get Build Numbers (VBA)](Get_Build_Numbers_Example_VB.htm)  
[Get Build Numbers (VB.NET)](Get_Build_Numbers_Example_VBNET.htm)  
[Get Build Numbers (C#)](Get_Build_Numbers_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md)  
[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md)  
[ISldWorks::IGetVersionHistoryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetVersionHistoryCount.md)  
[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.md)
