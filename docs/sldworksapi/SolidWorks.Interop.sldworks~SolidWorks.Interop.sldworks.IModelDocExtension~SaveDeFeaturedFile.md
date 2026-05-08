# SaveDeFeaturedFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDeFeaturedFile`

Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part.
Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveDeFeaturedFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveDeFeaturedFile(FileName)
```

```

System.bool SaveDeFeaturedFile( 
   System.string FileName
)
```

```

System.bool SaveDeFeaturedFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name for the new, de-featured part

#### Return Value

True if method call is successful; false otherwise

Example

[Save as De-Featured File (VBA)](Save_As_Defeatured_File_Example_VB.htm)  
[Save as De-Featured File (VB.NET)](Save_As_Defeatured_File_Example_VBNET.htm)  
[Save as De-Featured File (C#)](Save_As_Defeatured_File_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md)
