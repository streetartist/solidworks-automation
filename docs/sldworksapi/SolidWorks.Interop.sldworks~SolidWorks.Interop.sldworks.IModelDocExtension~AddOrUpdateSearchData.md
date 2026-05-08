# AddOrUpdateSearchData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrUpdateSearchData`

Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document.
Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddOrUpdateSearchData( _
   ByVal AppName As System.String, _
   ByVal AppKeyword As System.String, _
   ByVal AppValue As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim AppName As System.String
Dim AppKeyword As System.String
Dim AppValue As System.String
Dim value As System.Boolean
 
value = instance.AddOrUpdateSearchData(AppName, AppKeyword, AppValue)
```

```

System.bool AddOrUpdateSearchData( 
   System.string AppName,
   System.string AppKeyword,
   System.string AppValue
)
```

```

System.bool AddOrUpdateSearchData( 
   System.String^ AppName,
   System.String^ AppKeyword,
   System.String^ AppValue
) 
```

#### Parameters

*AppName*
:   Third-party application name

*AppKeyword*
:   Third-party application keyword

*AppValue*
:   Value for AppKeyword

#### Return Value

True if the SOLIDWORKS Search, third-party, application keyword and value are added to the model document, false if not

Remarks

After calling this method and after the keyword has been indexed in SOLIDWORKS Search, type the third-party application name, keyword, or keyword value in the SOLIDWORKS Search box and press Enter. Any documents assigned any of these three strings will appear on the Search tab in the Task Pane.

Example

[Add Third-party Application Keywords to SOLIDWORKS Search and Model (VBA)](Add_Third-party_Application_Keywords_to_SOLIDWORKS_Search_and_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSearchData.md)  
[IModelDocExtension::GetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchData.md)  
[IModelDocExtension::GetSearchDataCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSearchDataCount.md)  
[IModelDocExtension::IGetSearchData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSearchData.md)
