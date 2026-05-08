# AddSaveBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies`

Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk.
Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSaveBodies( _
   ByVal Bodies As System.Object, _
   ByVal FilePaths As System.Object _
) As System.Boolean
```

```

Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim FilePaths As System.Object
Dim value As System.Boolean
 
value = instance.AddSaveBodies(Bodies, FilePaths)
```

```

System.bool AddSaveBodies( 
   System.object Bodies,
   System.object FilePaths
)
```

```

System.bool AddSaveBodies( 
   System.Object^ Bodies,
   System.Object^ FilePaths
) 
```

#### Parameters

*Bodies*
:   Array of bodies to add to the Save Bodies feature

*FilePaths*
:   :   Array of path and filenames of part documents to which to save Bodies

#### Return Value

True if the bodies are added to the Save Bodies feature and saved as part documents on disk, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)  
[ISaveBodyFeatureData::GetSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.md)  
[ISaveBodyFeatureData::RemoveSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies.md)
