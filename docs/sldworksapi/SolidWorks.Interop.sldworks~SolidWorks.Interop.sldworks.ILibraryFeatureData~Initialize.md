# Initialize Method (ILibraryFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize`

Initializes a newly created library feature using the specified library part.
Initializes a newly created library feature using the specified library part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Initialize( _
   ByVal FileNameIn As System.String _
) As System.Boolean
```

```

Dim instance As ILibraryFeatureData
Dim FileNameIn As System.String
Dim value As System.Boolean
 
value = instance.Initialize(FileNameIn)
```

```

System.bool Initialize( 
   System.string FileNameIn
)
```

```

System.bool Initialize( 
   System.String^ FileNameIn
) 
```

#### Parameters

*FileNameIn*
:   Path and filename of the library part

#### Return Value

True if the library feature is initialized, false if not

Example

[Create Library Feature With References (C#)](Create_Library_Feature_With_References_Example_CSharp.htm)  
[Create Library Feature With References (VB.NET)](Create_Library_Feature_With_References_Example_VBNET.htm)  
[Create Library Feature With References (VBA)](Create_Library_Feature_With_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::LibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LibraryPart.md)  
[ILibraryFeatureData::LinkToLibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LinkToLibraryPart.md)
