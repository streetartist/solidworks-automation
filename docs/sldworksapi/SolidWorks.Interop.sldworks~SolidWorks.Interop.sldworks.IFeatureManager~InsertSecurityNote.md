# InsertSecurityNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSecurityNote`

Inserts a note for the specified macro feature.
Inserts a note for the specified [macro feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSecurityNote( _
   ByVal Text As System.String, _
   ByVal FeatureOwner As Feature _
) As Note
```

```

Dim instance As IFeatureManager
Dim Text As System.String
Dim FeatureOwner As Feature
Dim value As Note
 
value = instance.InsertSecurityNote(Text, FeatureOwner)
```

```

Note InsertSecurityNote( 
   System.string Text,
   Feature FeatureOwner
)
```

```

Note^ InsertSecurityNote( 
   System.String^ Text,
   Feature^ FeatureOwner
) 
```

#### Parameters

*Text*
:   Text for note

*FeatureOwner*
:   Macro feature for this note

#### Return Value

Point to [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) object

Remarks

The note is for display purposes only and cannot be modified by the end user. For example, you could display the note to inform an end user that editing or deleting the macro feature is prohibited.

You associate the note with the specified macro feature in:

- VB by using this method in the code that generates the macro feature and by setting swMacroFeatureSecurityEnableNote in the [macro feature's security function](sldworksAPIProgGuide.chm::/Macro_Features/Security_Function.htm). You should also include the conditions under which to display the note.
- C++ by using this method in the code that generates the macro feature and by setting swMacroFeatureSecurityEnableNote for the Options argument of [ISwComFeature::Security](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Security.md) in the [macro feature's security function](sldworksAPIProgGuide.chm::/Macro_Features/Security_Function.htm). You should also include the conditions under which to display the note.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
