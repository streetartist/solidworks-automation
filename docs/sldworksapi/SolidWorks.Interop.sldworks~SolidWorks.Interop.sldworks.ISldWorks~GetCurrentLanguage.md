# GetCurrentLanguage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLanguage`

Gets the current language used by SOLIDWORKS.
Gets the current language used by SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentLanguage() As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
value = instance.GetCurrentLanguage()
```

```

System.string GetCurrentLanguage()
```

```

System.String^ GetCurrentLanguage(); 
```

#### Return Value

Current language

Remarks

Possible return values are:

|  |  |  |
| --- | --- | --- |
| - chinese - chinese-simplified - czech - english - french | - german - italian - japanese - korean - polish | - portuguese-brazilian - russian - spanish - turkish |

You can see the current language in use by the SOLIDWORKS application in the SOLIDWORKS resources (dialogs, menus, and so on).

You can use the return value to set your local resource usage.

Example

[Get Language and Localized Menu Names (VBA)](Get_Language_and_Localized_Menu_Names_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
