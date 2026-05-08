# GetSaveBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies`

Gets the save bodies in this Save Bodies feature.
Gets the save bodies in this Save Bodies feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSaveBodies( _
   ByRef Bodies As System.Object, _
   ByRef FilePaths As System.Object, _
   ByRef Flags As System.Object _
) 
```

```

Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim Flags As System.Object
 
instance.GetSaveBodies(Bodies, FilePaths, Flags)
```

```

void GetSaveBodies( 
   out System.object Bodies,
   out System.object FilePaths,
   out System.object Flags
)
```

```

void GetSaveBodies( 
   [Out] System.Object^ Bodies,
   [Out] System.Object^ FilePaths,
   [Out] System.Object^ Flags
) 
```

#### Parameters

*Bodies*
:   :   Array of save bodies

*FilePaths*
:   Array of paths and filenames for the part documents of Bodies

*Flags*
:   :   Array of booleans indicating whether each corresponding save body is consumed; true if removed from the original part, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)  
[ISaveBodyFeatureData::GetSaveBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodiesCount.md)  
[ISaveBodyFeatureData::AddSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies.md)  
[ISaveBodyFeatureData::RemoveSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies.md)
