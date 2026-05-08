# GetSSOFormattedURL Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSSOFormattedURL`

Formats the specified URL for single sign-on.
Formats the specified URL for single sign-on.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSSOFormattedURL( _
   ByVal TargetUrl As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim TargetUrl As System.String
Dim value As System.String
 
value = instance.GetSSOFormattedURL(TargetUrl)
```

```

System.string GetSSOFormattedURL( 
   System.string TargetUrl
)
```

```

System.String^ GetSSOFormattedURL( 
   System.String^ TargetUrl
) 
```

#### Parameters

*TargetUrl*
:   URL to format

#### Return Value

URL formatted for single sign-on

Remarks

Use this method to log into SOLIDWORKS add-ins using the current SOLIDWORKS credentials.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
