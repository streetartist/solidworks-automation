# SaveTo3DExperience Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveTo3DExperience`

Saves this document in SOLIDWORKS Connected using the specified save options.
Saves this document in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) using the specified save options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveTo3DExperience( _
   ByVal Options As System.Object, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Options As System.Object
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean
 
value = instance.SaveTo3DExperience(Options, Errors, Warnings)
```

```

System.bool SaveTo3DExperience( 
   System.object Options,
   out System.int Errors,
   out System.int Warnings
)
```

```

System.bool SaveTo3DExperience( 
   System.Object^ Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
) 
```

#### Parameters

*Options*
:   [ISaveTo3DExperienceOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.md) (see **Remarks**)

*Errors*
:   Error codes

*Warnings*
:   Warning codes

#### Return Value

True if the document saved successfully, false if not

Remarks

If the file is:

- new and the file name is specified in Options, then this method acts like **File > Save**. If any other options are specified, then this method acts like **File > Save With Options**.
- already saved to the platform and a new file name is specified in Options, then this method acts like **File > Save As New**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
