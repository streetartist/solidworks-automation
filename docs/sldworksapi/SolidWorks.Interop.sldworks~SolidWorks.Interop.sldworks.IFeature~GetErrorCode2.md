# GetErrorCode2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2`

Gets the error code for this feature.
Gets the error code for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetErrorCode2( _
   ByRef IsWarning As System.Boolean _
) As System.Integer
```

```

Dim instance As IFeature
Dim IsWarning As System.Boolean
Dim value As System.Integer
 
value = instance.GetErrorCode2(IsWarning)
```

```

System.int GetErrorCode2( 
   out System.bool IsWarning
)
```

```

System.int GetErrorCode2( 
   [Out] System.bool IsWarning
) 
```

#### Parameters

*IsWarning*
:   True if the error is a warning, false if not

    **NOTE**: This parameter should only be examined if the return value is non-zero.

#### Return Value

Feature error code as defined in [swFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

Remarks

This method returns many of the errors indicated by the What's Wrong icon seen with an invalid feature in the FeatureManager design tree.

During feature creation, you can prevent the error dialog from appearing by using  
[IModelDoc2::ShowFeatureErrorDialog](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.md).

Example

[Get Error Codes for Features (VBA)](Get_Error_Codes_for_Features_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[ISldWorks::AllowFailedFeatureCreation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AllowFailedFeatureCreation.md)  
[IModelDoc2::ShowFeatureErrorDialog Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowFeatureErrorDialog.md)  
[IModelDocExtension::GetWhatsWrong Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.md)  
[IModelDocExtension::GetWhatsWrongCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrongCount.md)
