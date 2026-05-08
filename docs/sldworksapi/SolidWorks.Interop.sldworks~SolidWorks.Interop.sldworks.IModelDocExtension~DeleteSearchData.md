# DeleteSearchData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData`

Deletes the specified SOLIDWORKS Search third-party keywords from the model document.
Deletes the specified SOLIDWORKS Search third-party keywords from the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteSearchData( _
   ByVal AppName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim AppName As System.String
Dim value As System.Boolean
 
value = instance.DeleteSearchData(AppName)
```

```

System.bool DeleteSearchData( 
   System.string AppName
)
```

```

System.bool DeleteSearchData( 
   System.String^ AppName
) 
```

#### Parameters

*AppName*
:   Application name whose keywords to delete

#### Return Value

True if the keywords for AppName are deleted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::AddOrUpdateSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData.md)  
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.md)  
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.md)  
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.md)
