# GetSearchDataCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount`

Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document.
Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSearchDataCount( _
   ByVal AppName As System.String _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim AppName As System.String
Dim value As System.Integer
 
value = instance.GetSearchDataCount(AppName)
```

```

System.int GetSearchDataCount( 
   System.string AppName
)
```

```

System.int GetSearchDataCount( 
   System.String^ AppName
) 
```

#### Parameters

*AppName*
:   Third-party application name

#### Return Value

Number of keywords for AppName previously added to this model document

Remarks

Call this method before calling [IModelDocExtension::IGetSearchData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.md) to determine the size of the arrays for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.md)  
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.md)  
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.md)
