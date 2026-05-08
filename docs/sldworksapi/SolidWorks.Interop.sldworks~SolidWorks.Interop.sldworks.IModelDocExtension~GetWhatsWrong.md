# GetWhatsWrong Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong`

Gets the What's Wrong dialog information for this model document.
Gets the What's Wrong dialog information for this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWhatsWrong( _
   ByRef Features As System.Object, _
   ByRef ErrorCodes As System.Object, _
   ByRef Warnings As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Features As System.Object
Dim ErrorCodes As System.Object
Dim Warnings As System.Object
Dim value As System.Boolean
 
value = instance.GetWhatsWrong(Features, ErrorCodes, Warnings)
```

```

System.bool GetWhatsWrong( 
   out System.object Features,
   out System.object ErrorCodes,
   out System.object Warnings
)
```

```

System.bool GetWhatsWrong( 
   [Out] System.Object^ Features,
   [Out] System.Object^ ErrorCodes,
   [Out] System.Object^ Warnings
) 
```

#### Parameters

*Features*
:   Array of features in the What's Wrong dialog

*ErrorCodes*
:   Array of error codes corresponding to the features in the What's Wrong dialog as defined in [swFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

*Warnings*
:   :   Array of Booleans corresponding to the features in the What's Wrong dialog indicating whether SOLIDWORKS detected a What's Wrong item as a warning; true if SOLIDWORKS detected a What's Wrong item as a warning, false if not

#### Return Value

True if this method runs successfully, false if not

Example

[Get What's Wrong (C#)](Get_What's_Wrong_Example_CSharp.htm)  
[Get What's Wrong (VB.NET)](Get_What's_Wrong_Example_VBNET.htm)  
[Get What's Wrong (VBA)](Get_What's_Wrong_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetWhatsWrongCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrongCount.md)  
[IFeature::GetErrorCode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.md)  
[IMacroFeatureData::Provider Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.md)
